"""
@title: cozy_ex_dynamic
@author: amorano
@category: Example
@reference: https://github.com/cozy-comfyui/cozy_ex_dynamic
@tags: dynamic, example, developer, script, mechanism, exemplar
@description: Example of a Node with Dyanmic Inputs
@node list:
    CozyDynamicNode
@version: 1.0.0
"""

from typing import Any, Dict, Tuple

# =============================================================================
# === GLOBAL ===
# =============================================================================

NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}
WEB_DIRECTORY = "./web"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]

# =============================================================================
# === NODE ===
# =============================================================================

class DynamicNodeCozy:
    """
    A class to represent a dynamic node in ComfyUI.
    """
    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("IMAGE",)
    FUNCTION = "run"
    CATEGORY = "_EXAMPLES"

    @classmethod
    def INPUT_TYPES(s) -> Dict[str, dict]:
        return {
            "required": {},
            "optional": {}
        }

    def run(self, **kw) -> Tuple[Any | None]:
        # the dynamically created input data will be in the dictionary kwargs
        #for k, v in kw.items():
        #    print(f'{k} => {v}')

        # return the first value found or `None` if no inputs are defined
        value = None
        if len(values := kw.values()) > 0:
            value = next(iter(values))
        return (value,)

# =============================================================================
# === REGISTRATION ===
# =============================================================================

NODE_CLASS_MAPPINGS = {
    "DynamicNodeCozy": DynamicNodeCozy,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DynamicNodeCozy": "Dynamic Node (cozy)",
}
