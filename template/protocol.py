# The MIT License (MIT)
# Copyright © 2023 Yuma Rao
# TODO(developer): Set your name
# Copyright © 2023 <your name>

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the “Software”), to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of
# the Software.

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
# THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import typing
import bittensor as bt
import numpy as np

# TODO(developer): Rewrite with your protocol definition.

# This is the protocol for the dummy miner and validator.
# It is a simple request-response protocol where the validator sends a request
# to the miner, and the miner responds with a dummy response.

# ---- miner ----
# Example usage:
#   def dummy( synapse: Dummy ) -> Dummy:
#       synapse.dummy_output = synapse.dummy_input + 1
#       return synapse
#   axon = bt.axon().attach( dummy ).serve(netuid=...).start()

# ---- validator ---
# Example usage:
#   dendrite = bt.dendrite()
#   dummy_output = dendrite.query( Dummy( dummy_input = 1 ) )
#   assert dummy_output == 2


class Dummy(bt.Synapse):
    """
    A modified dummy protocol representation which uses bt.Synapse as its base.
    This protocol helps in handling request and response communication between
    the miner and the validator for a cellular automata simulation.

    For CA Dummy input should at least be the ruleset and the number of steps

    Attributes:
    - ruleset: An integer value representing the ruleset for the cellular automata simulation.
    - steps: An integer value representing the number of steps for the cellular automata simulation.
    - simulation_output: An optional 2D list of integers which, when filled, represents the result of the cellular automata simulation.
    """

    # Required request inputs, filled by sending dendrite caller.
    ruleset: int
    steps: int

    # Optional request output, filled by receiving axon.
    simulation_output: typing.Optional[bytes] = None

    def deserialize(self) -> np.ndarray:
        """
        Deserialize the simulation output. This method retrieves the result of
        the CA simulation from the miner in the form of simulation_output,
        deserializes it and returns it as the output of the dendrite.query() call.
        This should be more efficient for numerical ops than a list

        Returns:
        - np.ndarray: The deserialized response, which in this case is the value of simulation_output.
        """
        if self.simulation_output is not None:
            return np.frombuffer(self.simulation_output, dtype=np.int).reshape(-1, 100)
        else:
            return None
