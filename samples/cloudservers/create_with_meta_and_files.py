#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2012 Rackspace

# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import os
import pyrax

creds_file = os.path.expanduser("~/.rackspace_cloud_credentials")
pyrax.set_credential_file(creds_file)
cs = pyrax.cloudservers

ubu_image = [img for img in cs.images.list()
		if "12.04" in img.name][0]
flavor_512 = [flavor for flavor in cs.flavors.list()
		if flavor.ram == 512][0]

meta = {"test_key": "test_value",
        "meaning_of_life": "42",
        }

content = """This is the contents of the text file.
It has several lines of text.

And it even has a blank line."""

files = {"/root/testfile": content}

server = cs.servers.create("meta_server", ubu_image.id, flavor_512.id,
        meta=meta, files=files)
print "Name:", server.name
print "ID:", server.id
print "Admin Password:", server.adminPass
print "Metadata:", server.metadata
print
print "When the server becomes active, shell into it as root with the admin password."
print "Verify that the file '/root/testfile' exists, and contains the exact content"
print "that was defined above."
print
