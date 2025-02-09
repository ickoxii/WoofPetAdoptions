import { Button } from "@mui/material";
import { useChat } from "@/utils/contexts/chatContext";
import { Message } from "@mui/icons-material";

export default function ContactCard(props) {
    const { contactee, sender, defaultMessage = "", link = "" } = props;
    const { openChatByUser } = useChat();

    const handleContact = async (event) => {
        /* Send a message to contactee, if NULL then return
         */
        if (contactee == null) {
            return
        }
        openChatByUser(sender, contactee, defaultMessage, link) /* Opens a chat with contactee as receiver */
    }

    return (
        <Button
            variant="contained"
            color="primary"
            sx={{
                padding: "12px 12px",
                fontSize: "14px",
                minWidth: "175px",
                justifyContent: "space-evenly",
            }}
            onClick={handleContact} // Define this function for the different action
        >
            <Message></Message>
            Contact Center
        </Button>
    )
}