import imageService from './imageService';
import { useSelector } from "react-redux";

const apiUrl = process.env.NEXT_PUBLIC_API_URL;

const eventService = () => {
    const { uploadEventThumbnail } = imageService();
    const authenticationToken = useSelector((state) => state.authenticationToken.token);

    const createEvent = async (formData, thumbnailImage, centerId) => {
        console.log("Creating new event:", formData, centerId, thumbnailImage);
        const response = await fetch(`${apiUrl}/api/events/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${authenticationToken}`,
            },
            body: JSON.stringify({
                centerId: centerId,
                datePosted: formData.datePosted,
                name: formData.name,
                description: formData.description,
                dateStart: formData.dateStart,
                dateEnd: formData.dateEnd,
                address: formData.address,
                city: formData.city,
                state: formData.state,
            })
        });

        const result = await response.json();
        if (response.ok) {
            if (thumbnailImage != null) {
                const thumbnailResult = uploadEventThumbnail(thumbnailImage, result.eventID);
                if (thumbnailResult == null) {
                    console.log("Error uploading event thumbnail!");
                    return null;
                }
            }
            return result;
        } else {
            alert(`Event creation failed: ${result.message}`);
            return null;
        }
    };

    const getEventInfo = async (eventID) => {
        const response = await fetch(`${apiUrl}/api/events/${eventID}`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${authenticationToken}`,
            }
        });

        const result = await response.json();
        console.log(result);
        if (response.ok) {
            return result;
        } else {
            alert(`Get info failed: ${result.message}`);
            return null;
        }
    };


    const updateEvent = async (formData, thumbnail, eventID) => {
        const response = await fetch(`${apiUrl}/api/events/update/${eventID}`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${authenticationToken}`,
            },
            body: JSON.stringify({
                centerId: formData.centerId,
                datePosted: formData.datePosted,
                name: formData.name,
                description: formData.description,
                dateStart: formData.dateStart,
                dateEnd: formData.dateEnd,
                address: formData.address,
                city: formData.city,
                state: formData.state,
            })
        });

        const result = await response.json();
        if (response.ok) {
            if (thumbnail != null) {
                const thumbnailResult = await uploadEventThumbnail(thumbnail, eventID);
                if (thumbnailResult == null) {
                    return null;
                }
            }
            return result;
        } else {
            alert(`Update failed: ${result.message}`);
            return null;
        }
    };

    const deleteEvent = async (eventID) => {
        const response = await fetch(`${apiUrl}/api/events/${eventID}`, {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${authenticationToken}`,
            }
        });

        const result = await response.json();
        if (response.ok) {
            return result;
        } else {
            alert(`Delete Event failed: ${result.message}`);
            return null;
        }
    };

    const getCenterEvents = async (centerId) => {
        const response = await fetch(`${apiUrl}/api/events/center/${centerId}`, {
            method: 'GET',
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${authenticationToken}`,
            },
        });
        const result = await response.json();
        if (response.ok) {
            return result;
        } else {
            alert(`Getting events failed ${result.message}`);
            return null;
        }
    };

    const getEventsByPage = async (pageSize, pageNumber) => {
        const response = await fetch(`${apiUrl}/api/events/paginated?pageSize=${pageSize}&pageNumber=${pageNumber}`, {
            method: 'GET',
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${authenticationToken}`,
            },
        });

        const result = await response.json();
        if (response.ok) {
            return result;
        } else {
            console.error(`Getting events failed ${result.message}`);
            return null;
        }
    }


    return {
        createEvent,
        getEventInfo,
        updateEvent,
        deleteEvent,
        getCenterEvents,
        getEventsByPage,
    };

};

export default eventService;