import ipaddress

def detect_cidr_overlap(azure_cidrs, aws_cidrs):
    """
    Detects overlapping CIDR blocks between Azure and AWS.
    """
    all_cidrs = []
    all_cidrs.extend(azure_cidrs)
    all_cidrs.extend(aws_cidrs)

    # Convert all CIDRs to ipaddress.ip_network objects
    try:
        networks = [ipaddress.ip_network(cidr) for cidr in all_cidrs]
    except ValueError as e:
        return f"Error parsing CIDR: {e}"

    overlaps = []
    # Check for overlaps between all pairs of networks
    for i in range(len(networks)):
        for j in range(i + 1, len(networks)):
            if networks[i].overlaps(networks[j]):
                overlaps.append(f"Overlap detected: {networks[i]} and {networks[j]}")

    return overlaps

if __name__ == "__main__":
    # Example Azure CIDR blocks (e.g., VNet address spaces)
    # These are hypothetical and should be replaced with actual values.
    azure_vnet_cidrs = [
        "10.1.0.0/16",
        "192.168.10.0/24"
    ]

    # Example AWS CIDR blocks (e.g., VPC address spaces)
    # These are hypothetical and should be replaced with actual values.
    aws_vpc_cidrs = [
        "10.0.0.0/16",
        "172.16.0.0/12",
        "192.168.10.0/24" # This CIDR is intentionally overlapping
    ]

    print("--- Checking for CIDR Overlaps ---")

    # Combine and check for overlaps
    all_potential_cidrs = azure_vnet_cidrs + aws_vpc_cidrs
    overlap_results = detect_cidr_overlap(azure_vnet_cidrs, aws_vpc_cidrs)

    if not overlap_results:
        print("No CIDR overlaps detected between Azure and AWS plans.")
    else:
        print("The following CIDR overlaps were found:")
        for overlap in overlap_results:
            print(f"- {overlap}")

    print("\n--- Planning for Harmony ---")
    print("When migrating from Azure to AWS, careful CIDR planning is crucial.")
    print("Ensure that your Azure VNet address spaces and AWS VPC CIDR blocks do not overlap.")
    print("This script helps identify potential conflicts before they cause network issues.")
    print("Consider using non-overlapping private IP ranges (e.g., RFC 1918) for each cloud environment.")
