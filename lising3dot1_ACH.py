#listing3dot1_ACH
class ACHFileParser:
    def __init__(self, filename):
        self.filename = filename
        self.transactions = []

    def parse_file_header_record(self, line):
        priority_code = line[1:3]
        immediate_destination = line[3:13]
        # Continue parsing other fields...

    def parse_batch_header_record(self, line):
        service_class_code = line[1:4]
        company_name = line[4:20]
        # Continue parsing other fields...

    def parse_entry_detail_record(self, line):
        transaction_code = line[1:3]
        receiving_dfi_identification = line[3:12]
        check_digit = line[12]
        dfi_account_number = line[13:29]
        amount = line[29:39]
        individual_identification_number = line[39:54]
        individual_name = line[54:76]
        discretionary_data = line[76:78]
        addenda_record_indicator = line[78]
        trace_number = line[79:94]

        transaction = {
            'transaction_code': transaction_code,
            'receiving_dfi_identification': receiving_dfi_identification,
            'check_digit': check_digit,
            'dfi_account_number': dfi_account_number,
            'amount': amount,
            'individual_identification_number': individual_identification_number,
            'individual_name': individual_name,
            'discretionary_data': discretionary_data,
            'addenda_record_indicator': addenda_record_indicator,
            'trace_number': trace_number
        }

        self.transactions.append(transaction)

    def parse_ach_file(self):
        with open(self.filename, 'r') as file:
            lines = file.readlines()

        for line in lines:
            record_type_code = line[0]
            if record_type_code == '1':  # File Header Record
                self.parse_file_header_record(line)
            elif record_type_code == '5':  # Batch Header Record
                self.parse_batch_header_record(line)
            elif record_type_code == '6':  # Entry Detail Record
                self.parse_entry_detail_record(line)
            # Continue with other record types...

        return self.transactions