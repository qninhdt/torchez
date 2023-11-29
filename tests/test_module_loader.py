from torchez.module_loader import module


def test_module():
    assert module() == "module"
