#!/usr/bin/env python3
# Copyright 2023 Ubuntu
# See LICENSE file for licensing details.
#
# Learn more at: https://juju.is/docs/sdk

"""Charm the service.

Refer to the following post for a quick-start guide that will help you
develop a new k8s charm using the Operator Framework:

https://discourse.charmhub.io/t/4208
"""

import logging

import ops

# Log messages can be retrieved using juju debug-log
logger = logging.getLogger(__name__)

class FooCharm(ops.CharmBase):
    """Charm the service."""

    def __init__(self, *args):
        super().__init__(*args)
        self.framework.observe(self.on["provides"].relation_joined, self._on_relation_joined)
        self.framework.observe(self.on["provides"].relation_departed, self._on_relation_departed)
        self.framework.observe(self.on["requires"].relation_joined, self._on_relation_joined)
        self.framework.observe(self.on["requires"].relation_departed, self._on_relation_departed)

    def _on_relation_joined(self, event: ops.RelationJoinedEvent):
        event.relation.data[self.unit]["bar"] = "foobar"
        logger.debug(f"{event.relation.data=}")

    def _on_relation_departed(self, event: ops.RelationDepartedEvent):
        logger.error(f"{event.departing_unit=}, {event.relation.data=}")

if __name__ == "__main__":  # pragma: nocover
    ops.main(FooCharm)
