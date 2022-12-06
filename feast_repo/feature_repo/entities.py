from feast import Entity, ValueType

book = Entity(name="book", join_keys=["isbn"], value_type=ValueType.STRING)

user = Entity(name="user", join_keys=["user_id"], value_type=ValueType.INT64)
