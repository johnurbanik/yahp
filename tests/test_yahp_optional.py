import pytest

from tests.yahp_fixtures import OptionalFieldHparam, OptionalHparamsField, YamlInput


def test_empty_object_optional_field_hparams_data(optional_field_empty_object_yaml_input: YamlInput):
    o = OptionalFieldHparam.create_from_dict(data=optional_field_empty_object_yaml_input.dict_data)
    assert o.choice.maybe == 0  # type: ignore


def test_empty_object_optional_field_hparams_file(optional_field_empty_object_yaml_input: YamlInput):
    o = OptionalFieldHparam.create(filepath=optional_field_empty_object_yaml_input.filename)
    assert o.choice.maybe == 0  # type: ignore


def test_null_object_optional_field_hparams_data(optional_field_null_object_yaml_input: YamlInput):
    o = OptionalFieldHparam.create_from_dict(data=optional_field_null_object_yaml_input.dict_data)
    assert o.choice.maybe == 0  # type: ignore


def test_null_object_optional_field_hparams_file(optional_field_null_object_yaml_input: YamlInput):
    o = OptionalFieldHparam.create(filepath=optional_field_null_object_yaml_input.filename)
    assert o.choice.maybe == 0  # type: ignore


def test_optional_hparams_field():
    o = OptionalHparamsField()
    assert o.optional_hparams is None
