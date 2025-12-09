from src.domain.entities import Message


def parse_stored_conversation_to_openai_spec(conversation: list[Message]):
    parsed_conversation = []
    for message in conversation:
        parsed_conversation.append(
            {
                "role": "user" if message.emitter == "user" else "assistant",
                "content": message.text,
            }
        )
    return {"messages": parsed_conversation}


def parse_to_openai_spec(
    prompt: str, conversation: list[Message], new_interaction_text: str
):
    parsed_conversation = parse_stored_conversation_to_openai_spec(conversation)
    parsed_conversation["messages"].insert(0, {"role": "developer", "content": prompt})
    parsed_conversation["messages"].append(
        {"role": "user", "content": new_interaction_text}
    )
    return parsed_conversation
