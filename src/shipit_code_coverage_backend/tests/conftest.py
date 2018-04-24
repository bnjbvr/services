# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from __future__ import absolute_import

import pytest

import backend_common


@pytest.fixture(scope='session')
def app():
    '''Load shipit_code_coverage_backend in test mode
    '''
    import shipit_code_coverage_backend

    config = backend_common.testing.get_app_config({
    })
    app = shipit_code_coverage_backend.create_app(config)

    with app.app_context():
        backend_common.testing.configure_app(app)
        yield app