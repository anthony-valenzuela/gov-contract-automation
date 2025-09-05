"""
Send a document for signature using DocuSign API.
"""

from docusign_esign import ApiClient, EnvelopesApi, EnvelopeDefinition, Document, Signer, SignHere, Recipients

def send_for_signature(document_path, recipient_email, recipient_name):
    # Configure the DocuSign API client (use environment variables for security in practice)
    api_client = ApiClient()
    api_client.host = "https://demo.docusign.net/restapi"
    # Add JWT/authentication as per DocuSign API documentation

    with open(document_path, "rb") as file:
        doc_bytes = file.read()

    document = Document(
        document_base64=doc_bytes.encode("base64"),
        name="Contract",
        file_extension="pdf",
        document_id="1"
    )

    signer = Signer(
        email=recipient_email,
        name=recipient_name,
        recipient_id="1",
        routing_order="1"
    )

    sign_here = SignHere(
        anchor_string="**signature**",
        anchor_units="pixels",
        anchor_x_offset="0",
        anchor_y_offset="0"
    )

    signer.tabs = {"sign_here_tabs": [sign_here]}
    recipients = Recipients(signers=[signer])

    envelope_definition = EnvelopeDefinition(
        email_subject="Please sign this contract",
        documents=[document],
        recipients=recipients,
        status="sent"
    )

    envelopes_api = EnvelopesApi(api_client)
    results = envelopes_api.create_envelope(account_id="YOUR_ACCOUNT_ID", envelope_definition=envelope_definition)
    print("Envelope sent. Envelope ID:", results.envelope_id)

# For real use, implement authentication and error handling.
