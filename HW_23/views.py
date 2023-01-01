from typing import Dict, List, Optional, Iterable

from flask import Blueprint, request, jsonify, Response

from HW_23.builder import build_query
from HW_23.models import BatchRequestParams

main_bp = Blueprint('main', __name__)

FILE_NAME = '/home/pavel/PycharmProjects/HW_24/HW_23/data/apache_logs.txt'  # 'data/apache_logs.txt'
""" Написал абсолютный путь т.к.  на Ubuntu по другому не работало """


@main_bp.route('/perform_query', methods=['POST'])
def perform_query() -> Response:
    validated_data: Dict[str, List[Dict[str, str]]] = BatchRequestParams().load(data=request.json)
    result: Optional[Iterable[str]] = None
    for query in validated_data['queries']:
        result = build_query(
            cmd=query['cmd'],
            value=query['value'],
            file_name=FILE_NAME,
            data=result,
        )
    return jsonify(result)
