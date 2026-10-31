---
records:
    - id: KGB9VXFYW1
      kind: monograph
      title: Potential Theory
      creators:
        - name: Lester L. Helms
          role: author
      date: "2009"
      expressions:
        - key: e1
          kind: edition
          date: "2009"
          ids:
            doi:
                - 10.1007/978-1-4471-6422-7
                - 10.1007/978-1-84882-319-8
          manifestations:
            - key: m1
              kind: print
              publisher: Springer London
              date: "2014"
              ids:
                isbn:
                    - "9781447164210"
                    - "9781447164227"
            - key: m2
              kind: print
              publisher: Springer London
              date: "2009"
              ids:
                isbn:
                    - "9781848823181"
                    - "9781848823198"
      relations:
        - kind: part_of
          to: W0CC03QJC7
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4471-6422-7
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-84882-319-8
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
---
