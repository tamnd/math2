---
records:
    - id: CKD4FCAK8P
      kind: monograph
      title: Calculus of Variations
      creators:
        - name: Filip Rindler
          role: author
          ids:
            orcid: 0000-0003-2126-3865
      date: "2018"
      expressions:
        - key: e1
          kind: edition
          date: "2018"
          ids:
            doi:
                - 10.1007/978-3-032-24483-3
                - 10.1007/978-3-319-77637-8
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Nature Switzerland
              date: "2026"
              ids:
                isbn:
                    - "9783032244826"
                    - "9783032244833"
            - key: m2
              kind: print
              publisher: Springer International Publishing
              date: "2018"
              ids:
                isbn:
                    - "9783319776361"
                    - "9783319776378"
      relations:
        - kind: part_of
          to: 7ME1ABA6H5
          source: cluster/1
        - kind: part_of
          to: W0CC03QJC7
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-032-24483-3
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-319-77637-8
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
