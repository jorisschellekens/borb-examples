def add_action_annotations(page: Page):
    add_invisible_button(
        Rectangle(Decimal(275), Decimal(492), Decimal(13), Decimal(13)),
        "process_token('0')",
    )
    add_invisible_button(
        Rectangle(Decimal(291), Decimal(492), Decimal(13), Decimal(13)),
        "process_token('.')",
    )
    add_invisible_button(
        Rectangle(Decimal(307), Decimal(492), Decimal(13), Decimal(13)),
        "process_token('=')",
    )

    add_invisible_button(
        Rectangle(Decimal(275), Decimal(507), Decimal(13), Decimal(13)),
        "process_token('1')",
    )
    add_invisible_button(
        Rectangle(Decimal(291), Decimal(507), Decimal(13), Decimal(13)),
        "process_token('2')",
    )
    add_invisible_button(
        Rectangle(Decimal(307), Decimal(507), Decimal(13), Decimal(13)),
        "process_token('3')",
    )

    add_invisible_button(
        Rectangle(Decimal(275), Decimal(522), Decimal(13), Decimal(13)),
        "process_token('4')",
    )
    add_invisible_button(
        Rectangle(Decimal(291), Decimal(522), Decimal(13), Decimal(13)),
        "process_token('5')",
    )
    add_invisible_button(
        Rectangle(Decimal(307), Decimal(522), Decimal(13), Decimal(13)),
        "process_token('6')",
    )

    add_invisible_button(
        Rectangle(Decimal(275), Decimal(538), Decimal(13), Decimal(13)),
        "process_token('7')",
    )
    add_invisible_button(
        Rectangle(Decimal(291), Decimal(538), Decimal(13), Decimal(13)),
        "process_token('8')",
    )
    add_invisible_button(
        Rectangle(Decimal(307), Decimal(538), Decimal(13), Decimal(13)),
        "process_token('9')",
    )

    add_invisible_button(
        Rectangle(Decimal(324), Decimal(551), Decimal(13), Decimal(12)),
        "process_token('/')",
    )
    add_invisible_button(
        Rectangle(Decimal(324), Decimal(536), Decimal(13), Decimal(13)),
        "process_token('x')",
    )
    add_invisible_button(
        Rectangle(Decimal(324), Decimal(520), Decimal(13), Decimal(13)),
        "process_token('-')",
    )
    add_invisible_button(
        Rectangle(Decimal(324), Decimal(497), Decimal(13), Decimal(21)),
        "process_token('+')",
    )

    add_invisible_button(
        Rectangle(Decimal(257), Decimal(541), Decimal(13), Decimal(21)),
        "process_token('AC')",
    )
