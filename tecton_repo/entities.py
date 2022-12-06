from tecton import Entity

user = Entity(
    name='user',
    join_keys=['user_id'],
    owner='jake@tecton.ai',
    tags={'release': 'production'}
)

book = Entity(
    name='book',
    join_keys=['isbn'],
    owner='jake@tecton.ai',
    tags={'release': 'production'}
)
