class Cpu:
    def __init__(self, brand, model, core_number, thread_number, price):
        self.brand = brand
        self.model = model
        self.core_number = core_number
        self.thread_number = thread_number
        self.price = price

cpu_01 = Cpu( "AMD", "Ryzen 7 1800X", 8, 16, "189.93€" )
cpu_02 = Cpu( "Intel", "i5-8400", 6, 6, "182€" )
cpu_03 = Cpu( "intel", "Pentium G4560", 2, 4, "65€" )
cpu_04 = Cpu( "AMD", "Ryzen 2600X", 6, 12, "141€" )
cpu_05 = Cpu( "intel", "i7-9700K", 8, 8, "376€" )

cpuList = [ cpu_01, cpu_02, cpu_03, cpu_04, cpu_05]