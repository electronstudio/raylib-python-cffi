from pathlib import Path
import ast
import os


ROOT = Path(__file__).resolve().parents[1]
_DEFAULT_PYRAY_STUB = ROOT / "pyray" / "__init__.pyi"
_stub_override = os.environ.get("PYRAY_STUB_PATH")
PYRAY_STUB = (
    Path(_stub_override).expanduser()
    if _stub_override
    else _DEFAULT_PYRAY_STUB
)
if not PYRAY_STUB.is_absolute():
    PYRAY_STUB = ROOT / PYRAY_STUB


def _parse_stub() -> ast.Module:
    return ast.parse(PYRAY_STUB.read_text(encoding="utf-8"))


def _top_level_names(module: ast.Module) -> set[str]:
    names: set[str] = set()
    for node in module.body:
        if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            names.add(node.target.id)
        elif isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    names.add(target.id)
    return names


def test_stub_includes_expected_smoke_constants() -> None:
    module_names = _top_level_names(_parse_stub())
    required_names = {
        "RL_FUNC_ADD",
        "RL_ONE",
        "RL_ONE_MINUS_SRC_ALPHA",
        "RL_QUADS",
        "RL_SRC_ALPHA",
        "RL_ZERO",
    }
    assert required_names.issubset(module_names)


def test_stub_excludes_deprecated_shorthand_constants() -> None:
    module_names = _top_level_names(_parse_stub())
    omitted_names = {
        "ARROWS_SIZE",
        "BLEND_ALPHA",
        "MOUSE_BUTTON_LEFT",
        "SHADER_LOC_MATRIX_MVP",
        "SHADER_UNIFORM_FLOAT",
        "TEXTURE_FILTER_POINT",
    }
    assert omitted_names.isdisjoint(module_names)


def test_texture2d_is_a_texture_alias() -> None:
    module = _parse_stub()
    class_names = {
        node.name for node in module.body if isinstance(node, ast.ClassDef)
    }
    aliases: dict[str, str] = {}
    for node in module.body:
        if not isinstance(node, ast.Assign):
            continue
        if len(node.targets) != 1:
            continue
        target = node.targets[0]
        if isinstance(target, ast.Name) and isinstance(node.value, ast.Name):
            aliases[target.id] = node.value.id

    assert aliases.get("Texture2D") == "Texture"
    assert "Texture2D" not in class_names
