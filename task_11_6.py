# Продолжить работу над предыдущим заданием. Реализовать механизм валидации вводимых пользователем данных. 
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

from abc import ABC, abstractmethod

class Warehouse:

	inventory = {}

	@classmethod
	def __init__(cls, name, total_storage_space: int, occupied_storage_space: int):
		
		cls.name = name
		cls.total_storage_space = total_storage_space												#cbm
		cls.__occupied_storage_space = occupied_storage_space										#cbm

	@staticmethod
	def validate_int_args(*args):
		for el in args:
			if isinstance(el, str):
				print(f'All single numeric arguments must be integer type only. Particularly this one: {el}.')
				exit(1)

	@classmethod
	def accept_shipment(cls, cargo_qty, cargo_name, volume, shipment_number):

		Warehouse.validate_int_args(cls.total_storage_space, cls.__occupied_storage_space, cargo_qty, volume, shipment_number)

		if (cls.total_storage_space - cls.__occupied_storage_space) >= volume:
			inventory_name = cargo_name
			cls.inventory.setdefault(inventory_name, printer_1.parameters.copy())
			
			if shipment_number == 1:
				del cls.inventory[inventory_name]['quantity']
			
			cls.inventory[inventory_name].setdefault('accepted_qty')
			
			if cls.inventory[inventory_name]['accepted_qty'] == None:
				cls.inventory[inventory_name]['accepted_qty'] = 0
			
			cls.inventory[inventory_name]['accepted_qty'] += cargo_qty

			cls.__occupied_storage_space += volume
			print(f'The shipment of {cargo_name} in the amount of {cargo_qty} units has been accepted at warehouse {cls.name}.')
			
			return True
		
		else:
			print(f'There is no empty space for storage at this warehouse. We can accept only {cls.total_storage_space - cls.__occupied_storage_space}.\
 Pls decrease the volume of shipment or submit your request for acceptance after a while.')
			
			return False

	@classmethod
	def check_inventory_to_ship(cls, cargo_name, cargo_qty):
	
		if cargo_name in cls.inventory.keys():
			available_qty = cls.inventory[cargo_name]['accepted_qty']

			if available_qty >= cargo_qty:
				return True
			
			else:
				print(f'Not enough inventory of {cargo_name}. You can ship out only {available_qty}')
		
		else:

			print('No requested inventory stored at warehouse. Pls ship this item to warehouse first')

	@classmethod
	def ship_to_office(cls, cargo_name, cargo_qty, department_name):

		Warehouse.validate_int_args(cargo_qty)
		if Warehouse.check_inventory_to_ship(cargo_name, cargo_qty):
			if cargo_qty > 2:
				print('\nYou can ship max 2 units of one item to one department.')
			
			else:
				cls.inventory[cargo_name]['accepted_qty'] -= cargo_qty
				w, l, h = cls.inventory[cargo_name]['dimensions'].split('*')
				volume = float(w) * float(l) * float(h) * cargo_qty
				cls.__occupied_storage_space -= volume
				print(f'Your shipping request has been processed and confirmed. {cargo_qty}\
 items of {cargo_name} will be shipped to {department_name} today.')
	
	@classmethod
	@property
	def get_stocks(cls):
		for key in cls.inventory.keys():
			stock_qty = cls.inventory[key]['accepted_qty']
			print(f'{key}: {stock_qty} units')


class OfficeEquipment(ABC):

	shipment_number = 0

	@abstractmethod
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

		self.parameters = {'description': self.description,
						   'color':	self.color,
						   'speed':	self.speed,
						   'owner':	self.owner,
						   'quantity': self.quantity,
						   'vendor': self.vendor,
						   'model':	self.model,
						   'price': self.price,
						   'warranty': self.warranty,
						   'leadtime': self.leadtime,
						   'max_paper_size': self.max_paper_size,
						   'has_display': self.has_display,
						   'voltage': self.voltage,
						   'power': self.power,
						   'dimensions': self.dimensions,
						   'madein': self.madein,
						   'weight': self.weight,
						}
	
	@abstractmethod
	def ship_to_warehouse(self, cargo_qty):

		Warehouse.validate_int_args(self.quantity, cargo_qty)

		self.shipment_number += 1
		self.cargo_qty = cargo_qty
		self.cargo_name = f"{self.parameters.get('description')} {self.parameters.get('vendor')} {self.parameters.get('model')}"
		w, l, h = self.parameters.get('dimensions').split('*')
		volume = float(w) * float(l) * float(h) * cargo_qty
		response = Warehouse.accept_shipment(self.cargo_qty, self.cargo_name, volume, self.shipment_number)

		if response == True:
			self.parameters['quantity'] = self.parameters.get('quantity') - cargo_qty


class Printer(OfficeEquipment):
	
	shipment_number = 0

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

		self.parameters = {'description': self.description,
						   'color': self.color,
						   'speed': self.speed,
						   'owner': self.owner,
						   'quantity': self.quantity,
						   'vendor': self.vendor,
						   'model': self.model,
						   'price': self.price,
						   'warranty': self.warranty,
						   'leadtime': self.leadtime,
						   'max_paper_size': self.max_paper_size,
						   'has_display': self.has_display,
						   'voltage': self.voltage,
						   'power': self.power,
						   'dimensions': self.dimensions,
						   'madein': self.madein,
						   'weight': self.weight,
						   'printing_process': self.printing_process,
						   'inkcolor': self.inkcolor,
						   'can_print_photo': self.can_print_photo,
						   'dpi': self.dpi,
						   'supported_paper_types': self.supported_paper_types,
						   'auto_ds_printing': self.auto_ds_printing
						}

	def ship_to_warehouse(self, cargo_qty):

		Warehouse.validate_int_args(self.quantity, cargo_qty)

		self.shipment_number += 1
		self.cargo_qty = cargo_qty
		self.cargo_name = f"{self.parameters.get('description')} {self.parameters.get('vendor')} {self.parameters.get('model')}"
		w, l, h = self.parameters.get('dimensions').split('*')
		volume = float(w) * float(l) * float(h) * cargo_qty
		response = Warehouse.accept_shipment(self.cargo_qty, self.cargo_name, volume, self.shipment_number)

		if response == True:
			self.parameters['quantity'] = self.parameters.get('quantity') - cargo_qty


class Scanner(OfficeEquipment):
	
	shipment_number = 0

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

		self.parameters = {'description': self.description,
						   'color':	self.color,
						   'speed':	self.speed,
						   'owner':	self.owner,
						   'quantity': self.quantity,
						   'vendor': self.vendor,
						   'model':	self.model,
						   'price': self.price,
						   'warranty': self.warranty,
						   'leadtime': self.leadtime,
						   'max_paper_size': self.max_paper_size,
						   'has_display': self.has_display,
						   'voltage': self.voltage,
						   'power': self.power,
						   'dimensions': self.dimensions,
						   'madein': self.madein,
						   'weight': self.weight,
					   	   'formfactor': self.formfactor,
						   'scanning_sensor': self.scanning_sensor,
						   'dpi': self.dpi,
						   'auto_feeder': self.auto_feeder,
						   'tray_quantity': self.tray_quantity,
						   'auto_db_scanning': self.auto_db_scanning,
						   'scan_color_depth': self.scan_color_depth,
							}

	def ship_to_warehouse(self, cargo_qty):
		
		Warehouse.validate_int_args(self.quantity, cargo_qty)

		self.shipment_number += 1
		self.cargo_qty = cargo_qty
		self.cargo_name = f"{self.parameters.get('description')} {self.parameters.get('vendor')} {self.parameters.get('model')}"
		w, l, h = self.parameters.get('dimensions').split('*')
		volume = float(w) * float(l) * float(h) * cargo_qty
		response = Warehouse.accept_shipment(self.cargo_qty, self.cargo_name, volume, self.shipment_number)

		if response == True:
			self.parameters['quantity'] = self.parameters.get('quantity') - cargo_qty


class CopyMachine(OfficeEquipment):
	
		shipment_number = 0

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

			self.parameters = {'description': self.description,
							   'color':	self.color,
							   'speed':	self.speed,
							   'owner':	self.owner,
							   'quantity': self.quantity,
							   'vendor': self.vendor,
							   'model':	self.model,
							   'price': self.price,
							   'warranty': self.warranty,
							   'leadtime': self.leadtime,
							   'max_paper_size': self.max_paper_size,
							   'has_display': self.has_display,
							   'voltage': self.voltage,
							   'power': self.power,
							   'dimensions': self.dimensions,
							   'madein': self.madein,
							   'weight': self.weight,
							   'isprinter': self.isprinter,
							   'isscanner': self.isscanner,
							   'printing_process': self.printing_process,
							   'inkcolor': self.inkcolor,
							   'can_print_photo': self.can_print_photo,
							   'dpi': self.dpi,
							   'supported_paper_types': self.supported_paper_types,
							   'auto_ds_printing': self.auto_ds_printing,
							   'printing_speed': self.printing_speed,
							   'scanning_sensor': self.scanning_sensor,
							   'auto_feeder': self.auto_feeder,
							   'tray_quantity': self.tray_quantity,
							   'auto_db_scanning': self.auto_db_scanning,
							   'scan_color_depth': self.scan_color_depth,
							   'scanning_speed': self.scanning_speed,
								}

		def ship_to_warehouse(self, cargo_qty):
			
			Warehouse.validate_int_args(self.quantity, cargo_qty)

			self.shipment_number += 1
			self.cargo_qty = cargo_qty
			self.cargo_name = f"{self.parameters.get('description')} {self.parameters.get('vendor')} {self.parameters.get('model')}"
			w, l, h = self.parameters.get('dimensions').split('*')
			volume = float(w) * float(l) * float(h) * cargo_qty
			response = Warehouse.accept_shipment(self.cargo_qty, self.cargo_name, volume, self.shipment_number)

			if response == True:
				self.parameters['quantity'] = self.parameters.get('quantity') - cargo_qty

Warehouse('Kolomna FDC-1', 1000, 0)

printer_1 = Printer('printer', 'black', 30, 'IP Ivanov', 500, 'Xerox', 'MD-50', 
150000, 2, 8, 'A3', True, 16, 1, '0.4*0.3*0.2', 'China', 2, 
'laser', 'RGB', True, '300*300', 'A4, A3, A5', False)

printer_2 = Printer('printer', 'white', 20, 'IP Akopyan', 40, 'Brother', 'BP-34', 
20000, 2, 8, 'A3', True, 16, 1, '0.4*0.3*0.2', 'China', 2, 
'laser', 'RGB', True, '300*300', 'A4', False)

scanner_1 = Scanner('scanner', 'black', 30, 'IP Ivanov', 500, 'Xerox', 'SMD-650', 
150000, 2, 8, 'A3', True, 16, 1, '0.6*0.3*0.1', 'China', 400, 'pad', 'XMR-50', '300*300', True, 1, False, 50)

copy_machine_1 = CopyMachine('copying machine', 'grey', 100, 'OOO Mimikrichnye Sistemy', 1500, 'Xerox', 
'XPMD-200', 450000, 2, 10, 'A3', True, 16, 1, '1.5*0.5*0.6', 'Japan', 50, True, True, 'laser', 'mono', False, '700*700',
'A3, A4, A5, postcards, envelopes', True, 80, 'SUPERVISION-235', True, 3, True, 70, 50)


# отгружаем на склад
printer_1.ship_to_warehouse(30)
printer_1.ship_to_warehouse(70)
printer_2.ship_to_warehouse(10)
scanner_1.ship_to_warehouse(500)
copy_machine_1.ship_to_warehouse(1000)

# отгружаем со склада в офис
Warehouse.ship_to_office('printer Xerox MD-50', 2, 'sales department')
Warehouse.ship_to_office('printer Brother BP-34', 1, 'procurement department')
Warehouse.ship_to_office('scanner Xerox SMD-650', 2, 'sales department')
Warehouse.ship_to_office('copying machine Xerox XPMD-200', 2, 'sales department')

#проверяем остатки на складе:
Warehouse.get_stocks

#проверочка:
# print('%' * 50)
# print(printer_1.parameters)
# print('%' * 50)
# print(printer_2.parameters)
# print('%' * 50)
# print(scanner_1.parameters)
# print('%' * 50)
# print(copy_machine_1.parameters)
# print('%' * 50)
# print(Warehouse.inventory)


