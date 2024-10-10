import re

# Helper functions to map types between Scala and Python
def scala_to_python_type(scala_type: str) -> str:
    return {
        "String": "str",
        "Int": "int",
        "Double": "float",
        "Long": "int",
        "Boolean": "bool",
        "Float": "float",
        "Option[String]": "Optional[str]",
        "Option[Int]": "Optional[int]",
        "Option[Double]": "Optional[float]",
        "Option[Boolean]": "Optional[bool]",
        "Option[Long]": "Optional[int]",
        "Option[Float]": "Optional[float]"
    }.get(scala_type, "Any")

def scala_to_python(scala_code: str) -> str:
    # Match class name and fields in Scala case class
    class_name_match = re.search(r'case class (\w+)\((.*?)\)', scala_code, re.DOTALL)

    if not class_name_match:
        raise ValueError("Invalid Scala case class definition")

    class_name = class_name_match.group(1)
    fields_str = class_name_match.group(2)

    # Extract field names and types
    fields = [field.strip() for field in fields_str.split(',')]
    field_list = []

    for field in fields:
        field_name, scala_type = field.split(':')
        field_name = field_name.strip()
        scala_type = scala_type.strip()
        python_type = scala_to_python_type(scala_type)
        field_list.append(f"{field_name}: {python_type}")

    # Generate Python dataclass
    python_class = f"@dataclass\nclass {class_name}:\n"
    python_class += "    " + "\n    ".join(field_list)
    return f"from dataclasses import dataclass\nfrom typing import Optional, Any\n\n{python_class}"