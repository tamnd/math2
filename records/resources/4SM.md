---
records:
    - id: 4SM6PWVH3S
      kind: monograph
      title: Proof Theory
      creators:
        - name: Kurt Schütte
          role: author
      date: "1977"
      msc:
        - code: 03F99
          from: zbmath_search
        - code: 03-02
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1977"
          ids:
            doi: 10.1007/978-3-642-66473-1
            zbl: "0367.02012"
            zbl_id: "3572133"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1977"
              ids:
                isbn:
                    - "9783642664755"
                    - "9783642664731"
              access:
                class: record
      relations:
        - kind: part_of
          to: GQFCNY816R
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-642-66473-1
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "3572133"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.13 scope/1
          note: from in to in
    - id: 4SMZCYMG40
      kind: problem-set
      title: Putnam 2005
      creators:
        - name: Mathematical Association of America
          role: author
      date: "2005"
      msc:
        - code: 00A07
          from: putnam
        - code: 97U40
          from: putnam
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2005"
          structure: 4SMZCYMG40/e1.json
      relations:
        - kind: part_of
          to: TYDZDDC2MA
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: putnam
          snapshot: blake3:a8efce689e279311a280a90aaaac925d4b96f7c8ccdd9eb1e8fb29b48d574603
          native_id: "2005"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.13 scope/1
          note: from in to in
---
