
class DeleteAppointment(Action):
    """
    Delete an appointment from a calendar
    """
    def run(self, ldap_profile, delete_dn):
        raise NotImplementedError
