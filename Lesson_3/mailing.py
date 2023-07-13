from address import Address

class Mailing:
    to_address: Address = 'unknown'
    from_address: Address = 'unknown'
    cost: int = '0'
    track: str = '12345'

    def __init__(self, to_adr, fr_adr, cost, track):
        self.to_address = to_adr
        self.from_address = fr_adr
        self.cost = cost
        self.track = track

    