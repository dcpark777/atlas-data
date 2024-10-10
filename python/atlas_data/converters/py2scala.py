

def python_to_scala_type(python_type: str) -> str:
    return {
        "str": "String",
        "int": "Int",
        "float": "Double",
        "bool": "Boolean",
        "Optional[str]": "Option[String]",
        "Optional[int]": "Option[Int]",
        "Optional[float]": "Option[Double]",
        "Optional[bool]": "Option[Boolean]"
    }.get(python_type, "Any")

def python_to_scala(python_code: str) -> str:
    # Match class name and fields in Python dataclass
    class_name_match = re.search(r'@dataclass\s+class (\w+):\s+(.*)', python_code, re.DOTALL)

    if not class_name_match:
        raise ValueError("Invalid Python dataclass definition")

    class_name = class_name_match.group(1)
    fields_str = class_name_match.group(2)

    # Extract field names and types
    fields = re.findall(r'(\w+):\s+(\w+[\[\]\w]*)', fields_str)
    field_list = []

    for field_name, python_type in fields:
        scala_type = python_to_scala_type(python_type)
        field_list.append(f"{field_name}: {scala_type}")

    # Generate Scala case class
    scala_class = f"case class {class_name}(\n    "
    scala_class += ",\n    ".join(field_list) + "\n)"
    return scala_class