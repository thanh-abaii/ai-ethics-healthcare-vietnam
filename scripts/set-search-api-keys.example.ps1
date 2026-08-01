# Copy these assignments into the current PowerShell session. Do not save real
# values in this file, a repository file, an artifact, terminal transcript, or chat.

$env:NCBI_API_KEY = '<your NCBI API key>'
$env:POLITE_EMAIL = '<your institutional contact email>' # accepted by both PubMed and OpenAlex
$env:OPENALEX_API_KEY = '<your OpenAlex API key>'
$env:OPENALEX_MAILTO = '<your institutional contact email>'

# Verify presence only; this command must never print secret values.
[pscustomobject]@{
    NCBI_API_KEY_PRESENT = -not [string]::IsNullOrWhiteSpace($env:NCBI_API_KEY)
    NCBI_CONTACT_EMAIL_PRESENT = -not [string]::IsNullOrWhiteSpace($env:NCBI_CONTACT_EMAIL)
    OPENALEX_API_KEY_PRESENT = -not [string]::IsNullOrWhiteSpace($env:OPENALEX_API_KEY)
    OPENALEX_MAILTO_PRESENT = -not [string]::IsNullOrWhiteSpace($env:OPENALEX_MAILTO)
}
