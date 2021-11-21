# This is a sample Python script.

def dec_to_bin(x):
    result = ""
    octetLength = len(bin(x)[2:])
    # if octetLength < 8:  #redundant
    for i in range(0, 8 - octetLength):
        result += "0"
    return f"{result}{int(bin(x)[2:])}"


def address_to_binary(address):
    new_address = []
    for octet in address:
        new_address.append(dec_to_bin(int(octet)))
    return new_address


def calc_network_address_pairs(addr1, addr2):
    result = ""
    for n, m in zip(addr1, addr2):
        result = result + str(int(n) * int(m))
    return result


def calculate_network_address_list(address, subnet):
    network_address = []
    for count in enumerate(address):
        network_address.append(calc_network_address_pairs(address[count[0]], subnet[count[0]]))
    return network_address


def calculate_network_broadcast(address, subnet):
    not_subnet = []
    broadcast_address = []
    for number in subnet:
        temp = number.replace('1', 'a')
        temp = temp.replace('0', 'b')
        temp = temp.replace('a', '0')
        temp = temp.replace('b', '1')
        not_subnet.append(temp)

    print(not_subnet)
    print(bin_to_int(not_subnet[3]))
    for count in enumerate(address):
        temp_pair = int(bin_to_int(address[count[0]])) + int(bin_to_int(not_subnet[count[0]]))
        broadcast_address.append(temp_pair)
    return broadcast_address


def address_to_dec(addr1):
    address = []
    for count in enumerate(addr1):
        temp = int(bin_to_int(addr1[count[0]]))
        address.append(temp)
    return address


def calculate_host_number(subnet):
    shortened_mask = 0
    for octet in subnet:
        for bit in octet:
            shortened_mask += int(bit)
    return pow(2, 32-shortened_mask) - 2


def bin_to_int(x):
    result = 0
    for count in enumerate(x):
        result += int(count[1]) * pow(2, len(x) - 1 - count[0])
    return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # calculate network address
    # calculate broadcast address
    # calculate host number
    # calculate first
    # calculate last
    ipaddress = '172.16.160.200'
    subnet_mask = '255.255.192.0'

    temp_network_address = address_to_dec(calculate_network_address_list(address_to_binary(ipaddress.split(sep='.')), address_to_binary(subnet_mask.split(sep='.'))))
    network_address = ".".join([str(int) for int in temp_network_address])
    broadcast = ".".join([str(int) for int in calculate_network_broadcast(address_to_binary(network_address.split(sep='.')), address_to_binary(subnet_mask.split(sep='.')))])
    first = ".".join([str(int) for int in address_to_dec(calculate_network_address_list(address_to_binary(ipaddress.split(sep='.')), address_to_binary(subnet_mask.split(sep='.'))))[:3]])
    last = ".".join([str(int) for int in calculate_network_broadcast(address_to_binary(network_address.split(sep='.')), address_to_binary(subnet_mask.split(sep='.')))[:3]])


    print(f"Given HOST IP address: {ipaddress}\n"
          f"subnet mask: {subnet_mask}\n"
          f"\n+---------------------------------------------------------------------+\n"
          f"| network address:   {network_address}\n"
          f"| broadcast address: {broadcast}\n"
          f"| available hosts:   {calculate_host_number(address_to_binary(subnet_mask.split(sep='.')))}\n"
          f"| first host address: {first}, {address_to_dec(calculate_network_address_list(address_to_binary(ipaddress.split(sep='.')), address_to_binary(subnet_mask.split(sep='.'))))[3] + 1}\n"
          f"| last host address: {last}, {calculate_network_broadcast(address_to_binary(network_address.split(sep='.')), address_to_binary(subnet_mask.split(sep='.')))[3] - 1}\n"
          f"+---------------------------------------------------------------------+\n"
          f"\nhave a nice networking!")
