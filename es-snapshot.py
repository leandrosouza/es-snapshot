#!/usr/bin/env python

import sys
import logging
import argparse
from elasticsearch import Elasticsearch


class ElasticSearchClient(object):
	LOG = logging.getLogger('elastic-search-client')

	def __init__(self, endpoint, indice_name):
		self.endpoint = endpoint
		self.indice_name = indice_name

	def output(self, msg):
		print(msg)

	def open_connection(self):
		connection = Elasticsearch([self.endpoint])
		return connection

	def exists(self):
		self.LOG.info('exists called with indice %s', self.indice_name)
		es = self.open_connection()
		result = es.indices.exists(self.indice_name)
		self.output('Exist' if result else 'Not found')

	def restore(self):
		self.LOG.info('restore called')

	def snapshot(self):
		self.LOG.info('snapshot called')

	def list(self):
		self.LOG.info('list called')


def main():
	parser = argparse.ArgumentParser(description='Process some integers.')
	parser.add_argument('command', choices=['restore', 'snapshot', 'exists'])
	parser.add_argument('indice_name')
	parser.add_argument('--endpoint', required=True)
	parser.add_argument('--logging', required=False, choices=['ERROR', 'WARN', 'INFO', 'DEBUG'], default='WARN')
	args = parser.parse_args()

	logging.basicConfig(level=getattr(logging, args.logging))
	client = ElasticSearchClient(endpoint=args.endpoint, indice_name=args.indice_name)
	getattr(client, args.command)()


if __name__ == '__main__':
	main()
