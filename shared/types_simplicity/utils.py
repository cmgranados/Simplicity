from shared.types_simplicity.models import TypeClassification, Type
from simplicity_main.constants import MyConstants


def get_datatypes_types():
    constants = MyConstants()
    dt_type_code = constants.DATATYPE_TYPE_CLASSIFICATION_CODE
    type_classification_dt = TypeClassification.objects.get(code = dt_type_code)
    dt_type_list = Type.objects.filter(type_classification_id = 
                                       type_classification_dt.type_classification_id)
    return dt_type_list