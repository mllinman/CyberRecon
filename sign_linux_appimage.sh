#!/bin/bash
# Sign the AppImage with GPG

APPIMAGE="CyberReconSuite_v1.3_RC.AppImage"
GPG_KEY="your-key-id"

gpg --detach-sign --armor --local-user "$GPG_KEY" "$APPIMAGE"
echo "Signature created: $APPIMAGE.asc"