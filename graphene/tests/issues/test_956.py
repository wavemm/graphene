from graphene.types.enum import _Enum


def test_issue():
    options = {"description": "This my enum", "deprecation_reason": "For the funs"}
    new_enum = _Enum("MyEnum", [("some", "data")], **options)
    assert new_enum._meta.description == options["description"]
    assert new_enum._meta.deprecation_reason == options["deprecation_reason"]
