from rest_framework.pagination import PageNumberPagination

class MyPageNumberPagination(PageNumberPagination):
    page_size = 1
    page_query_param = 'pg'

    # defines how much records to be fetched per page, this can be customer defined
    # page_size_query_param = 'records'
    # user defined page size cant be greater than 7
    # max_page_size = 7
    # what string must be used to define last page takes string as well as list of strings
    # last_page_strings=['last','end']