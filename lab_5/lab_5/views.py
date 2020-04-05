from django.shortcuts import render, redirect
from django.views.generic import TemplateView

import numpy as np


class Lab5Pt1(TemplateView):
    template_name = 'lab_numpy/lab5pt1.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['n'] = 7
        self.generate_data_in_context(context)
        return context


    def generate_float_array(self, n):
        return list(map(lambda i: round(i, 3), np.random.random(n)))

    def generate_int_array(self, min, max, n):
        return np.random.randint(min, max + 1, size=n)

    def get_result(self, arr):
        print(arr)
        result = 1        
        first_position_for_min = min(np.where(arr==min(arr, key=abs))[0])
        last_position_for_min = max(np.where(arr==min(arr, key=abs))[0])
        first_position_for_max = min(np.where(arr==max(arr, key=abs))[0])
        last_position_for_max = max(np.where(arr==max(arr, key=abs))[0])
        first_position = first_position_for_min
        last_position = last_position_for_max
        if first_position > last_position:
            first_position = first_position_for_max
            last_position = last_position_for_min
        if first_position+1 == last_position:
            return "Немає елементів між знайденими"                 
        else:
            for x in range(first_position+1, last_position):
                result *= arr[x]                
        return round(result, 5)
    
    def generate_data_in_context(self, context):
        n = context['n']
        context['range_n'] = range(n)
        context['array_1'] = self.generate_float_array(n)
        context['array_2'] = self.generate_int_array(-10, 10, n)
        context['array_3'] = self.generate_int_array(0, 50, n)
        context['result_1'] = self.get_result(context['array_1'])
        context['result_2'] = self.get_result(context['array_2'])
        context['result_3'] = self.get_result(context['array_3'])

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        context = self.get_context_data()

        n = request.GET.get('n', None)

        if n is not None:
            n = int(n)
            context['n'] = n
        self.generate_data_in_context(context)

        return render(request, self.template_name, context)


class Lab5Pt2(TemplateView):
    template_name = 'lab_numpy/lab5pt2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['n'] = 2
        context['m'] = 7
        self.generate_data_in_context(context)
        return context


    def generate_float_array(self, n, m):
        return np.random.random(size=(n, m)).round(3)

    def generate_int_array(self, min, max, n, m):
        return np.random.randint(min, max + 1, size=(n, m))

    def get_result(self, arr):
        result = arr.copy()
        for row_n in range(len(result)):
            min_abs_element = min(result[row_n], key=abs)
            for item in range(len(result[row_n])) :
                print(result[row_n][item])
                result[row_n][item] = round(result[row_n][item]*min_abs_element, 5)
                print(result[row_n][item])
                # import pdb
                # pdb.set_trace()
        return result
    
    def generate_data_in_context(self, context):
        n = context['n']
        m = context['m']

        context['range_n'] = range(n)
        context['range_m'] = range(m)
        context['matrix_1'] = self.generate_float_array(n, m)
        context['matrix_2'] = self.generate_int_array(-10, 10, n, m)
        context['matrix_3'] = self.generate_int_array(0, 50, n, m)
        context['matrix_1_result'] = self.get_result(context['matrix_1'])
        context['matrix_2_result'] = self.get_result(context['matrix_2'])
        context['matrix_3_result'] = self.get_result(context['matrix_3'])


    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        context = self.get_context_data()
        if n := request.GET.get('n', None):
            n = int(n)
            context['n'] = n
        if m := request.GET.get('m', None):
            m = int(m)
            context['m'] = m

        self.generate_data_in_context(context)

        return render(request, self.template_name, context)
    