// chat-store.ts
import {createStore} from 'zustand/vanilla'
import {Message} from "@/context/data/chat-model";

export type ChatState = {
    messages: Message[]
}

export type ChatActions = {
    addMessage: (message: Message) => void
}

export type ChatStore = ChatState & ChatActions

export const initChatState = (): ChatState => {
    return {
        messages: [],
    }
}

export const defaultInitState: ChatState = {
    messages: [],
}

export const createChatStore = (
    initState: ChatState = defaultInitState,
) => {
    return createStore<ChatStore>()((set) => ({
        ...initState,
        addMessage: (message: Message) => set((state) => ({
            messages: [...state.messages, message],
        })),
    }))
}