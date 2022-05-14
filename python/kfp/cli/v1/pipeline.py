from typing import Dict, List

from kfp.v2 import dsl


@dsl.component
def echo(
    no_default_param: int,
    int_param: int = 1,
    float_param: float = 1.5,
    str_param: str = "string_value",
    bool_param: bool = True,
    list_param: List[int] = [1, 2, 3],
    dict_param: Dict[str, int] = {"key": 4},
) -> str:
    return (
        f"no_default_param={no_default_param}({type(no_default_param)}), "
        f"int_param={int_param}({type(int_param)}), "
        f"float_param={float_param}({type(float_param)}), "
        f"str_param={str_param}({type(str_param)}), "
        f"bool_param={bool_param}({type(bool_param)}), "
        f"list_param={list_param}({type(list_param)}), "
        f"dict_param={dict_param}({type(dict_param)})"
    )


@dsl.pipeline(name="echo-pipeline")
def pipeline(
    no_default_param: int,
    int_param: int = 1,
    float_param: float = 1.5,
    str_param: str = "string_value",
    bool_param: bool = True,
    list_param: List[int] = [1, 2, 3],
    dict_param: Dict[str, int] = {"key": 4},
):
    echo(
        no_default_param=no_default_param,
        int_param=int_param,
        float_param=float_param,
        str_param=str_param,
        bool_param=bool_param,
        list_param=list_param,
        dict_param=dict_param,
    )
