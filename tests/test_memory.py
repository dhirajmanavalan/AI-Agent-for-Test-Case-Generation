from src.memory.memory_module import MemoryModule

def test_memory():
    memory = MemoryModule()

    memory.save("login", ["TC1"])

    result = memory.retrieve("login")

    assert result == ["TC1"]

# Check: Memory saves and retrieves correctly