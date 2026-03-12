import torch
import random

class V7V8Bridge:

    def __init__(self, field):

        self.field = field

    def translate(self, council_result):

        confidence = council_result["confidence"]

        decision = council_result["synthesis"]

        turbulence = random.uniform(0,1) * (1-confidence)

        influence = confidence * 0.2

        return {
            "decision":decision,
            "energy":influence,
            "turbulence":turbulence
        }

    def inject(self, bridge_signal):

        energy = bridge_signal["energy"]

        noise = torch.randn_like(self.field.field)*bridge_signal["turbulence"]

        self.field.field += energy + noise

        self.field.field.clamp_(-5,5)
