# -*- coding: utf-8 -*-

import os
import unittest

import intelmq.lib.test as test
import intelmq.lib.utils as utils

from intelmq.bots.parsers.nothink.parser_dns_attacks import NothinkDNSAttackParserBot

with open(os.path.join(os.path.dirname(__FILE__), 'honeypot_dns_attacks.txt')) as handle:
    EXAMPLE_FILE = handle.read()

EXAMPLE_REPORT = {'feed.url': 'http://www.nothink.org/honeypot_dns_attacks.txt',
                  'feed.name': 'DNS Attacks',
                  '__type': 'Report',
                  'raw': utils.base64_encode(EXAMPLE_FILE),
                  'time.observation': '2016-11-22T08:26:00+00:00'
                  }

EXAMPLE_EVENT = {'feed.url': 'http://www.nothink.org/honeypot_dns_attacks.txt',
                 'feed.name': 'DNS Attacks',
                 '__type': 'Event',
                 'raw': 'JzIwMTYtMTEtMTEgMTU6MTM6MjAnLCAnMTg2LjIuMTY3LjE0JywgJzI2MjI1NCcsICdEQU5DT00gTFRELCwsIEJaJywgJ2Rkb3MtZ3VhcmQubmV0JywgJ0JaJw==',
                 'time.source': '2016-11-11T15:13:20+00:00',
                 'source.ip': '186.2.167.14',
                 'source.asn': '262254',
                 'source.as_name': 'DANCOM LTD,,, BZ',
                 'source.reverse_dns': 'ddos-guard.net',
                 'source.geolocation.cc': 'BZ',
                 'classification.type': 'ddos',
                 'event_description.text': 'On time.source the source.ip was seen performing '
                                           'DNS amplification attacks against honeypots',
                 'protocol.application': 'dns'
                 }

class TestNothinkDNSAttackParserBot(test.BotTestCase, unittest.TestCase):
    """ A TestCase for NothinkDNSAttackParserBot """

    @classmethod
    def set_bot(cls):
        cls.bot_reference = NothinkDNSAttackParserBot
        cls.default_input_message = EXAMPLE_REPORT

    def test_event(self):
        """ Test if correct Event has been produced """
        self.run_bot()
        self.assertMessageEqual(0, EXAMPLE_EVENT)

if __name__ == '__main__':
    unittest.main()