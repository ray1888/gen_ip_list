# coding=utf-8


def all():
    configs = read_config()
    result = []
    for config in configs:
        result.append(gen_ip(config))
    output_result(result)
    print("gen_result_done")

def read_config():
    with open('batch_instal_ip_list.txt', 'r') as f:
        data = f.read()
        data = data.split('\n')
    return data

def output_result(result):
    with open('batch_install_ip_list_new.txt', 'w') as f:
        f.write('\n'.join(result))
    print("gen_ip_new_config_is done")


def gen_ip(ipitem):
    """
    :param ipitem: is strings like "10.10.10.125-129'
    :return:
    """
    item_split = ipitem.split('.')
    count_list = []
    counter = 0
    for item in item_split:
        if '-' in item:
            count_list.append(counter)
            counter += 1
    if counter == 1:
        single_dash_gen()
    elif counter == 2:
        double_dash_gen()
    elif counter == 3:
        triple_dash_gen()
    elif counter == 4:
        fourth_dash_gen()


def gen_recursive(prefix, gen, subfix_dict, itype='normal'):
    if not prefix:
        pass
    else:
        pass
    r_list = []
    if itype == "normal":
        sorted_keys = sorted(subfix_dict['normal'].keys())
    elif itype == "special":
        sorted_keys = sorted(subfix_dict['special'].keys())
    elif itype == "end":
        sorted_keys = sorted(subfix_dict['end'].keys())
    leng_subfix = len(sorted_keys)
    tmp_result = {}
    for i in leng_subfix:
        if i not in tmp_result.keys():
            tmp_result[i] = []
        if i == leng_subfix[0]:
            prefix = gen
        else:
            prefix = tmp_result[i-1]
        for item in subfix_dict[itype][i]:
            if isinstance(prefix, list):
                for single_prefix in prefix:
                    tmp_result[i].append('{0}.{1}'.format(single_prefix, item))
            else:
                tmp_result[i].append('{0}.{1}'.format(prefix, item))
    return tmp_result[leng_subfix]


def single_dash_gen(ip, count_list):
    ip_split = ip.split('.')
    if count_list[0] == 3:
        # tested
        origin_ip = '.'.join(ip_split[:3])
        start, end = ip_split[3].split('-')
        if end == '255' or start == "0":
            raise ValueError("over flow")
        gen_dash_list = range(int(start), int(end)+1)
        return_list = []
        for gen_number in gen_dash_list:
            return_list.append('{0}.{1}'.format(origin_ip, gen_number))
        return return_list
    else:
        # tested
        counter = count_list[0]
        origin_ip_prefix, origin_ip_subfix = ip_split[:counter], ip_split[counter+1:]
        if origin_ip_prefix:
            ip_prefix = '.'.join(origin_ip_prefix)
        else:
            ip_prefix = None
        return_list = []
        start, end = ip_split[counter].split('-')
        if end == '255' or start == "0":
            raise ValueError("over flow")
        gen_dash_list = range(int(start), int(end))
        if len(origin_ip_subfix) == 1:
            ip_special_subfix = range(int(origin_ip_subfix), 255)
            ip_normal_subfix = range(1, 255)
            ip_end_subfix = range(1, int(origin_ip_subfix))
            for gen_number in gen_dash_list:
                if gen_number == gen_dash_list[0]:
                    round_list = ip_special_subfix
                elif gen_number == gen_dash_list[len(gen_dash_list) - 1]:
                    round_list = ip_normal_subfix
                else:
                    round_list = ip_end_subfix
                for subfix in round_list:
                    return_list.append("{0}.{1}.{2}".format(ip_prefix, gen_number, subfix))
            return return_list
        else:
            ## TODO to be test
            subfix = {}
            subfix['normal'] = {}
            subfix['special'] = {}
            subfix['end'] = {}
            for i in range(0, len(origin_ip_subfix)):
                subfix['normal'][counter + i] = range(1, 255)
                subfix['special'][counter + i] = range(int(origin_ip_subfix[i]), 255)
                subfix['end'][counter + i] = range(1, origin_ip_subfix[i])
            for gen_number in gen_dash_list:
                if gen_number == gen_dash_list[0]:
                    special_result = gen_recursive(ip_prefix, gen_number, subfix, 'special')
                    return_list.append()
                elif gen_number == gen_dash_list[len(gen_dash_list) - 1]:
                    end_result = gen_recursive(ip_prefix, gen_number, subfix, 'end')
                    return_list.append()
                else:
                    normal_result = gen_recursive(ip_prefix, gen_number, subfix, 'normal')
                    return_list.append()
            return return_list

def double_dash_gen(ip, count_list):
    ip_split = ip.split('.')
    if count_list == [2, 3]:
        # Tested
        origin_ip = '.'.join(ip_split[:2])
        start1, end1 = ip_split[2].split('-')
        start, end = ip_split[3].split('-')
        if (end == '255' or start == "0") or (end1 =='255' or start1 == "0"):
            raise ValueError("over flow")
        gen_dash_list1 = range(int(start1), int(end1)+1)
        gen_dash_list = range(int(start), int(end)+1)
        return_list = []
        for gen_number1 in gen_dash_list1:
            for gen_number in gen_dash_list:
                return_list.append('{0}.{1}.{2}'.format(origin_ip, gen_number1, gen_number))
        return return_list
    else:
        # [0,1], [1,2]
        ## TODO to be filled
        counter = count_list(len(count_list)-1)
        origin_ip_prefix = ip_split[counter:]
        # origin_ip_subfix = ip_split[:co]

def triple_dash_gen(ip, count_list):
    # Tested
    ip_split = ip.split('.')
    if count_list == [1, 2, 3]:
        origin_ip = '.'.join(ip_split[:2])
        start2, end2 = ip_split[1].split('-')
        start1, end1 = ip_split[2].split('-')
        start, end = ip_split[3].split('-')
        if (end == '255' or start == "0") or (end1 =='255' or start1=="0") or (end2 =='255' or start2=="0"):
            raise ValueError("over flow")
        gen_dash_list2 = range(int(start2), int(end2)+1)
        gen_dash_list1 = range(int(start1), int(end1)+1)
        gen_dash_list = range(int(start), int(end)+1)
        return_list = []
        for gen_number2 in gen_dash_list2:
            for gen_number1 in gen_dash_list1:
                for gen_number in gen_dash_list:
                 return_list.append('{0}.{1}.{2}.{3}'.format(origin_ip, gen_number2, gen_number1, gen_number))
        return return_list
    else:
        origin_ip = ip_split[3:][0]
        start2, end2 = ip_split[1].split('-')
        start1, end1 = ip_split[2].split('-')
        start, end = ip_split[0].split('-')
        if (end == '255' or start == "0") or (end1 == '255' or start1 == "0") or (end2 == '255' or start2 == "0"):
            raise ValueError("over flow")
        gen_dash_list2 = range(int(start2), int(end2) + 1)
        gen_dash_list1 = range(int(start1), int(end1) + 1)
        gen_dash_list = range(int(start), int(end) + 1)
        len_list2 = len(gen_dash_list2)
        len_list1 = len(gen_dash_list1)
        len_list = len(gen_dash_list)
        gen_origin_speical = range(int(origin_ip), 255)
        gen_origin_end = range(1, int(origin_ip))
        gen_origin_normal = range(1, 255)
        return_list = []
        for gen_number2 in gen_dash_list2:
            for gen_number1 in gen_dash_list1:
                for gen_number in gen_dash_list:
                    if gen_number2 != gen_dash_list2[0] and gen_number1 != gen_dash_list1[0] and gen_number != gen_dash_list[0]:
                        gen_end = gen_origin_speical
                    elif gen_number2 != gen_dash_list2[len_list2-1] and gen_number1 != gen_dash_list1[len_list1-1] and gen_number != gen_dash_list[len_list-1]:
                        gen_end = gen_origin_end
                    else:
                        gen_end = gen_origin_normal
                    for item in gen_end:
                        return_list.append('{0}.{1}.{2}.{3}'.format(gen_number, gen_number2, gen_number1,  item))
        return return_list

def fourth_dash_gen(ip, count_list=[1,2,3,4]):
    # tested
    ip_split = ip.split('.')
    start3, end3 = ip_split[0].split('-')
    start2, end2 = ip_split[1].split('-')
    start1, end1 = ip_split[2].split('-')
    start, end = ip_split[3].split('-')
    if (end == '255' or start == "0") or (end1 == '255' or start1 == "0") or (end2 == '255' or start2 == "0") or(
        end3 == '255' or start3 == "0"
    ):
        raise ValueError("over flow")
    gen_dash_list2 = range(int(start2), int(end2) + 1)
    gen_dash_list1 = range(int(start1), int(end1) + 1)
    gen_dash_list = range(int(start), int(end) + 1)
    gen_dash_list3 = range(int(start3), int(end3)+1)
    return_list = []
    for gen_number3 in gen_dash_list3:
        for gen_number2 in gen_dash_list2:
            for gen_number1 in gen_dash_list1:
                for gen_number in gen_dash_list:
                    return_list.append('{0}.{1}.{2}.{3}'.format(gen_number3, gen_number2, gen_number1, gen_number))
    return return_list
