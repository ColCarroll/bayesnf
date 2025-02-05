# Copyright 2024 The bayesnf Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Copyright 2023 Google LLC

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     https://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""bayesnf API."""

# A new PyPI release will be pushed everytime `__version__` is increased
# When changing this, also update the CHANGELOG.md
__version__ = '0.1.0'

# pylint: disable=useless-import-alias,g-bad-import-order
from .bayesnf import dataset_config as dataset_config
from .bayesnf import models as models
from .bayesnf import inference as inference
from .bayesnf import spatiotemporal as spatiotemporal
from .bayesnf import evaluate as evaluate
# pylint: enable=useless-import-alias,g-bad-import-order

__all__ = [
    'dataset_config',
    'evaluate',
    'inference',
    'models',
    'spatiotemporal',]
