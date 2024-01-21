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

# Step 1. Import the necessary libraries and modules
import time
import cellpylib as cpl

# Bittensor
import bittensor as bt

# Bittensor Validator Template:
import template
from template.validator import forward

# import base validator class which takes care of most of the boilerplate
from template.base.validator import BaseValidatorNeuron


class Validator(BaseValidatorNeuron):
    """
    Your validator neuron class. You should use this class to define your validator's behavior. In particular, you should replace the forward function with your own logic.

    This class inherits from the BaseValidatorNeuron class, which in turn inherits from BaseNeuron. The BaseNeuron class takes care of routine tasks such as setting up wallet, subtensor, metagraph, logging directory, parsing config, etc. You can override any of the methods in BaseNeuron if you need to customize the behavior.

    This class provides reasonable default behavior for a validator such as keeping a moving average of the scores of the miners and using them to set weights at the end of each epoch. Additionally, the scores are reset for new hotkeys at the end of each epoch.
    """    
    
    def __init__(self, config=None):
        super(Validator, self).__init__(config=config)
        self.ruleset = None  # ruleset for the current epoch
        self.steps = None   # steps for the current epoch
        bt.logging.info("load_state()")
        self.load_state()

        # TODO(developer): Anything specific to your use case you can do here

    async def forward(self):
        """
        Validator forward pass. Consists of:
        - Generating the query
        - Querying the miners
        - Getting the responses
        - Rewarding the miners
        - Updating the scores
        """
        # Generate the query
        query = self.generate_query() # TODO - SAR create a function that (randomly?) generates the params (ruleset, steps) for the current epoch
        
        # Run the cellular automata simulation for the validator generated params
        ca = self.run_ca_simulation()

    # Compare the simulation results with the responses from the miners
    # ...
        # TODO(developer): Rewrite this function based on your protocol definition.
        return await forward(self)


    class Validator(BaseValidatorNeuron):
        # method to set the ruleset and the number of steps dynamically. Can be called whenever you need to update the current ruleset and steps
        # Can be called from anywhere you have access to the validator object. Method is async so should be call with 'await' from asynchronous context. 
        # If we need to call this method from a synchronous context (SAR is not sure!), we can just remove the 'async' keyword and call it normally.
        async def set_ruleset_and_steps(self, ruleset, steps):
            self.ruleset = ruleset
            self.steps = steps

        def run_ca_simulation(self):
            """
            Runs a simulation of the cellular automata for the current epoch.
            """
            # Run the CA simulation
            self.ca = cpl.init_simple2d(self.ruleset, self.steps)
            ca = cpl.evolve2d(ca, timesteps=self.steps, apply_rule=lambda n, c, t: cpl.totalistic_rule(n, k=self.ruleset))
            
            return ca




# The main function parses the configuration and runs the validator.
if __name__ == "__main__":
    with Validator() as validator:
        while True:
            bt.logging.info("Validator running...", time.time())
            time.sleep(5)
