---
records:
    - id: 7GWKAGMDPF
      kind: monograph
      title: Essential Topology
      creators:
        - name: Martin D. Crossley
          role: author
      date: "2005"
      msc:
        - code: 55-01
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2005"
          ids:
            doi: 10.1007/1-84628-194-6
            zbl: "1079.55001"
            zbl_id: "2198522"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer London
              date: "2005"
              ids:
                isbn:
                    - "9781852337827"
                    - "9781846281945"
              access:
                class: record
      relations:
        - kind: part_of
          to: 3YXAC8SZBF
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 dev scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/1-84628-194-6
          level: work
        - source: zbmath_search
          snapshot: blake3:25dd7c4358839cf7c8c9f5d07f0562e94f38728153e7db2255a7191282b967c2
          native_id: "2198522"
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
