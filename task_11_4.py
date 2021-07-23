# Начать работу над проектом «Склад оргтехники». Создать класс, описывающий склад. 
# А также класс «Оргтехника», который будет базовым для классов-наследников. 
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). 
# В базовом классе определить параметры, общие для приведённых типов. 
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class Warehouse:

	def __init__(self, name, total_storage_space, occupied_storage_space):

		self.total_storage_space = total_storage_space
		self.occupied_storage_space = occupied_storage_space


class OfficeEquipment:

	def __init__(self, description, color, speed, owner, quantity, vendor, 
		model, price, warranty, leadtime, max_paper_size, has_display, 
		voltage, power, dimensions, madein, weight):

		self.description = description
		self.color = color
		self.speed = speed
		self.owner = owner
		self.quantity = quantity
		self.vendor = vendor
		self.model = model
		self.price = price
		self.warranty = warranty
		self.leadtime = leadtime
		self.max_paper_size = max_paper_size
		self.has_display = has_display, 
		self.voltage = voltage
		self.power = power
		self.dimensions = dimensions
		self.madein = madein
		self.weight = weight


class Printer(OfficeEquipment):

	def __init__(self, description, color, speed, owner, quantity, 
		vendor, model, price, warranty, leadtime, max_paper_size, 
		has_display, voltage, power, 
		dimensions, madein, weight, printing_process, inkcolor, 
		can_print_photo, dpi, supported_paper_types, auto_ds_printing):

		super().__init__(description, color, speed, owner, quantity, vendor, 
			model, price, warranty, leadtime, max_paper_size, has_display,
			voltage, power, dimensions, madein, weight)

		self.printing_process = printing_process
		self.inkcolor = inkcolor
		self.can_print_photo = can_print_photo
		self.dpi = dpi
		self.supported_paper_types = supported_paper_types
		self.auto_ds_printing = auto_ds_printing


class Scanner(OfficeEquipment):

	def __init__(self, description, color, speed, owner, quantity, vendor, 
		model, price, warranty, leadtime, max_paper_size, has_display, 
		voltage, power, dimensions, madein, weight, 
		formfactor, scanning_sensor, dpi, auto_feeder, tray_quantity, 
		auto_db_scanning, scan_color_depth):

		super().__init__(description, color, speed, owner, quantity, vendor, 
			model, price, warranty, leadtime, max_paper_size, has_display, 
			voltage, power, dimensions, madein, weight)

		self.formfactor = formfactor
		self.scanning_sensor = scanning_sensor
		self.dpi = dpi
		self.auto_feeder = auto_feeder
		self.tray_quantity = tray_quantity
		self.auto_db_scanning = auto_db_scanning
		self.scan_color_depth = scan_color_depth


class CopyMachine(OfficeEquipment):
	
		def __init__(self, description, color, speed, owner, quantity, 
		vendor, model, price, warranty, leadtime, max_paper_size, 
		has_display, voltage, power, dimensions, 
		madein, weight, isprinter, isscanner, printing_process, inkcolor, 
		can_print_photo, dpi, supported_paper_types, auto_ds_printing, 
		printing_speed, scanning_sensor, auto_feeder, tray_quantity, 
		auto_db_scanning, scan_color_depth, scanning_speed):

			super().__init__(description, color, speed, owner, quantity, vendor, 
				model, price, warranty, leadtime, max_paper_size, has_display, 
				voltage, power, dimensions, madein, weight)

			self.isprinter = isprinter
			self.isscanner = isscanner
			self.printing_process = printing_process
			self.inkcolor = inkcolor
			self.can_print_photo = can_print_photo
			self.dpi = dpi
			self.supported_paper_types = supported_paper_types
			self.auto_ds_printing = auto_ds_printing
			self.printing_speed = printing_speed
			self.scanning_sensor = scanning_sensor
			self.auto_feeder = auto_feeder
			self.tray_quantity = tray_quantity
			self.auto_db_scanning = auto_db_scanning
			self.scan_color_depth = scan_color_depth
			self.scanning_speed = scanning_speed

#проверочка:

warehouse_1 = Warehouse('Kolomna FDC-1', 1000, 0)

display_1 = OfficeEquipment('display', 'black', '60Ghz', 'OOO Kupi Monitor', 500, 'Samsung', 
'GTZOP-17-16', 30000, None, 40, None, True, 5, 0.3, '0.4*0.27*0.05', 'Thailand', 0.7)

scanner_1 = Scanner('printer', 'black', 30, 'IP Ivanov', 500, 'Xerox', 'MD-50', 
150000, 2, 8, 'A3', True, 16, 1, '0.6*0.3*0.1', 'China', 400, 'pad', 'XMR-50', '300*300', True, 1, False, 50)

printer_1 = Printer('scanner', 'white', 20, 'IP Akopyan', 40, 'Brother', 'BP-34', 
20000, 2, 8, 'A3', True, 16, 1, '0.4*0.3*0.2', 'China', 2, 
'laser', 'RGB', True, '300*300', 'A4', False)

copy_machine_1 = CopyMachine('copying machine', 'grey', 100, 'OOO Mimikrichnye Sistemy', 1500, 'Xerox', 
'XPMD-200', 450000, 2, 10, 'A3', True, 16, 1, '1,5*0.5*0.6', 'Japan', 50, True, True, 'laser', 'mono', False, '700*700',
'A3, A4, A5, postcards, envelopes', True, 80, 'SUPERVISION-235', True, 3, True, 70, 50)
