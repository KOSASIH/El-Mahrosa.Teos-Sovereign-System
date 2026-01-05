import ast
from typing import Dict
from .policy_schema import SovereignPolicy
from .exceptions import PolicyViolation

class SafeEvaluator(ast.NodeVisitor):
    allowed_nodes = (
        ast.Expression, ast.BoolOp, ast.Compare,
        ast.Name, ast.Load, ast.Constant,
        ast.And, ast.Or, ast.Gt, ast.Lt, ast.Eq,
        ast.GtE, ast.LtE, ast.NotEq
    )

    def visit(self, node):
        if not isinstance(node, self.allowed_nodes):
            raise PolicyViolation(f"Unsafe policy expression: {type(node)}")
        return super().visit(node)

def safe_eval(expr: str, context: Dict):
    tree = ast.parse(expr, mode="eval")
    SafeEvaluator().visit(tree)
    return eval(compile(tree, "<policy>", "eval"), {}, context)

class PolicyEngine:
    def __init__(self, policy: SovereignPolicy):
        self.policy = policy

    def evaluate(self, context: Dict) -> str:
        for rule in self.policy.rules:
            if safe_eval(rule.condition, context):
                if rule.action.lower() == "deny":
                    raise PolicyViolation(rule.reason, rule.severity)
                return rule.action
        return "allow"
