def print_separator(title=None):
    """Print a separator line with optional title"""
    if title:
        print(f"\n{'='*20} {title} {'='*20}")
    else:
        print("\n" + "="*50)
    print()