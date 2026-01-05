from typing import Dict

class StateRegistry:
    _state: Dict[str, str] = {}

    @classmethod
    def set_state(cls, entity_id: str, state: str):
        cls._state[entity_id] = state

    @classmethod
    def get_state(cls, entity_id: str) -> str:
        return cls._state.get(entity_id, "active")
