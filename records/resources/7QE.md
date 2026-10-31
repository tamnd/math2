---
records:
    - id: 7QEGRM5AP9
      kind: monograph
      title: Computational Invariant Theory
      creators:
        - name: Harm Derksen
          role: author
        - name: Gregor Kemper
          role: author
      date: "2002"
      expressions:
        - key: e1
          kind: edition
          date: "2002"
          ids:
            doi:
                - 10.1007/978-3-662-04958-7
                - 10.1007/978-3-662-48422-7
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "2002"
              ids:
                isbn:
                    - "9783642077968"
                    - "9783662049587"
            - key: m2
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "2015"
              ids:
                isbn:
                    - "9783662484203"
                    - "9783662484227"
      relations:
        - kind: part_of
          to: XGZPMQ7BSM
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-662-04958-7
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-662-48422-7
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
