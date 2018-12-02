# coding=utf-8


import unittest
import ddt

from gen_ip import *

single_dash = ['10.10.10.130-195', '10.10.10.250-255', '10.10.10.130-254', ' 10.10.10.1-130', '10.10.10.0-130']

double_dash = ['10.10.1-254.1-254', '10.10.0-255.0-255', '10.10.1-254.0-255', '10.10.0-255.1-254']

triple_dash = ['10.195-230.10-230.1-254', '10.230-255.10-230.1-254', '10.195-230.0-255.1-254',
               '10.195-230.1-235.0-255', '10.195-230.0-255.0-255', '10.0-255.0-255.1-30',
               '10.0-255.0-255.0-255']

fourth_dash = ['10-192.195-230.10-230.1-254', '10-192.230-255.10-230.1-254', '10-192.195-230.0-255.1-254',
               '10-192.195-230.1-235.0-255', '10-192.195-230.0-255.0-255', '10-192.0-255.0-255.1-30',
               '10-192.0-255.0-255.0-255', '192-255.230-255.10-230.1-254']


dobule_dash2 = ['10.1-254.1-254.10', '10.0-255.0-255.10', '10.1-254.0-255.10', '10.0-255.1-254.10']
dobule_dash3 = ['10.10.1-254.1-254', '10.10.0-255.0-255', '10.10.1-254.0-255', '10.10.0-255.1-254']

triple_dash2 = ['10-15.20-21.30-31.5']
single_dash_3 = []
single_dash_2 = []
single_dash_1 = []

@ddt.ddt
class TestGenIp(unittest.TestCase):

    # @ddt.data(single_dash)
    # def test_with_one_single_dash_in_last(self, data):
    #     for ip in data:
    #         try:
    #             value = single_dash_gen(ip, [3])
    #             # self.assertEqual(value, ip)
    #             print(value)
    #             print("\n")
    #         except ValueError as e:
    #             print("is 0 or 255")
    #             continue
    #
    # @ddt.data(double_dash)
    # def test_with_two_dash_in_two_list(self, data):
    #     for ip in data:
    #         try:
    #             value = triple_dash_gen(ip, [1, 2, 3])
    #             # self.assertEqual(value, ip)
    #             print(value)
    #             print("\n")
    #         except ValueError as e:
    #             print("is 0 or 255")
    #             continue
    #
    # @ddt.data(triple_dash)
    # def test_with_three_dash_in_last_three(self, data):
    #     for ip in data:
    #         try:
    #             value = triple_dash_gen(ip, [1, 2, 3])
    #             # self.assertEqual(value, ip)
    #             print(value)
    #             print("\n")
    #         except ValueError as e:
    #             print("is 0 or 255")
    #             continue
    #
    # @ddt.data(fourth_dash)
    # def test_with_four_dash(self, data):
    #     for ip in data:
    #         try:
    #             value = fourth_dash_gen(ip, [0, 1, 2, 3])
    #             # self.assertEqual(value, ip)
    #             print(value)
    #             print("\n")
    #         except ValueError as e:
    #             print("is 0 or 255")
    #             continue

    # @ddt.data()
    # def test_with_two_dash_in_two_middle(self, data):
    #     pass
    #
    # @ddt.data()
    # def test_with_two_dash_in_two_first(self, data):
    #     pass

    @ddt.data(triple_dash2)
    def test_with_three_dash_in_first_three(self, data):
        for ip in data:
            try:
                value = triple_dash_gen(ip, [0, 1, 2])
                # self.assertEqual(value, ip)
                print(value)
                print("\n")
            except ValueError as e:
                print("is 0 or 255")
                continue


    # @ddt.data()
    # def test_with_single_dash_in_last_two(self, data):
    #     for ip in data:
    #         try:
    #             value = single_dash_gen(ip, [2])
    #             # self.assertEqual(value, ip)
    #             print(value)
    #             print("\n")
    #         except ValueError as e:
    #             print("is 0 or 255")
    #             continue
    #
    # @ddt.data()
    # def test_with_single_dash_in_last_three(self, data):
    #     for ip in data:
    #         try:
    #             value = single_dash_gen(ip, [1])
    #             # self.assertEqual(value, ip)
    #             print(value)
    #             print("\n")
    #         except ValueError as e:
    #             print("is 0 or 255")
    #             continue
    #
    # @ddt.data()
    # def test_with_single_dash_in_first(self, data):
    #     for ip in data:
    #         try:
    #             value = single_dash_gen(ip, [0])
    #             # self.assertEqual(value, ip)
    #             print(value)
    #             print("\n")
    #         except ValueError as e:
    #             print("is 0 or 255")
    #             continue
