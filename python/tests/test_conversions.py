

def test_scala_to_python_conversion():
    # Scala to Python Example
    scala_case_class = """
    case class Person(name: String, age: Int, salary: Option[Double])
    """

    print("Scala to Python conversion:\n")
    print(scala_to_python(scala_case_class))

def test_python_to_scala_conversion():
    # Python to Scala Example
    python_dataclass = """
    @dataclass
    class Person:
        name: str
        age: int
        salary: Optional[float]
    """

    print("\nPython to Scala conversion:\n")
    print(python_to_scala(python_dataclass))