# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.7.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v1alpha1_rule import V1alpha1Rule


class TestV1alpha1Rule(unittest.TestCase):
    """ V1alpha1Rule unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1alpha1Rule(self):
        """
        Test V1alpha1Rule
        """
        model = kubernetes.client.models.v1alpha1_rule.V1alpha1Rule()


if __name__ == '__main__':
    unittest.main()
