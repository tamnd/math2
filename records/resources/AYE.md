---
records:
    - id: AYEPND6TAA
      kind: monograph
      title: A Readable Introduction to Real Mathematics
      creators:
        - name: Daniel Rosenthal
          role: author
        - name: David Rosenthal
          role: author
        - name: Peter Rosenthal
          role: author
      date: "2014"
      expressions:
        - key: e1
          kind: edition
          date: "2014"
          ids:
            doi:
                - 10.1007/978-3-030-00632-7
                - 10.1007/978-3-319-05654-8
          manifestations:
            - key: m1
              kind: print
              publisher: Springer International Publishing
              date: "2018"
              ids:
                isbn:
                    - "9783030006310"
                    - "9783030006327"
            - key: m2
              kind: print
              publisher: Springer International Publishing
              date: "2014"
              ids:
                isbn:
                    - "9783319056531"
                    - "9783319056548"
      relations:
        - kind: part_of
          to: NWQC4TW7S9
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.2 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-030-00632-7
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-319-05654-8
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
