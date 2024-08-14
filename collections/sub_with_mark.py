import collections, re

item_order = collections.OrderedDict()


def code_with_exam(n):
    for i in range(n):
        sub_marks_list = input("Enter the subject with marks :").strip().split()
        subject_name = sub_marks_list[0]
        subject_mark = sub_marks_list[1]
        if subject_name not in item_order:
            item_order[subject_name] = subject_mark
        else:
            item_order[subject_name] = item_order[subject_name] + subject_mark
    return dict(item_order)


n = int(input("Number of subjects: "))
print(code_with_exam(n))
