"""
File: html_display_nodes.py
Author: MVU
Version: 57.0 (Stable & Correct Return Types)
Description: 
    - FIX: 'bool is not iterable'. Устранен баг при выполнении (Queue Prompt).
           Все значения в 'ui' теперь корректно обернуты в списки.
"""

from typing import Any, Dict, Tuple

class MVUHTMLDisplayNode:
    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        return {
            "required": {
                "text_content": ("STRING", {
                    "multiline": True,
                    "default": "<h3>MVU Node</h3><p>Ready.</p>",
                    "dynamicPrompts": False,
                    "placeholder": "HTML..."
                }),
                "css_content": ("STRING", {
                    "multiline": True,
                    "default": "body { color: white; }",
                    "dynamicPrompts": False,
                    "placeholder": "CSS..."
                }),
                # В Python мы просто определяем этот виджет. JS управляет им.
                "view_mode": ("BOOLEAN", {
                    "default": True,
                    "label_on": "View",
                    "label_off": "Edit"
                }),
            },
        }

    RETURN_TYPES: Tuple[Any, ...] = ()
    FUNCTION: str = "process"
    OUTPUT_NODE: bool = True
    CATEGORY: str = "MVU/Visualization"

    def process(self, text_content, css_content, view_mode):
        # --- CRITICAL FIX ---
        # ComfyUI требует, чтобы все значения в 'ui' были списками.
        # Раньше `mode` был просто bool, теперь это `[bool]`.
        return {
            "ui": {
                "html": [text_content],
                "css": [css_content],
                "mode": [view_mode] # <--- Вот здесь было исправление
            }
        }

# Экспорт
NODE_CLASS_MAPPINGS = { "MVU_HTML_Display": MVUHTMLDisplayNode }
NODE_DISPLAY_NAME_MAPPINGS = { "MVU_HTML_Display": "MVU HTML Display 🖥️" }